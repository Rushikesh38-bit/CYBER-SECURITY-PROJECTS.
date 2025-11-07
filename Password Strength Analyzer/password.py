import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from itertools import product
from datetime import datetime
from zxcvbn import zxcvbn
import os

# --- Leetspeak Mapping (Same as before) ---
LEET_MAP = {
    'a': ['4', '@', 'A'],
    'e': ['3', 'E'],
    'i': ['1', '!', 'I'],
    'o': ['0', 'O'],
    's': ['5', '$', 'S'],
    't': ['7', '+', 'T']
}

# --- Core Logic Functions ---

def analyze_password_logic(password, user_inputs_str):
    """Core logic for password analysis, returns results as a string."""
    if not password:
        return "⚠️ Please enter a password to analyze."

    # Parse user inputs (split by space or comma)
    user_inputs = [i.strip() for i in user_inputs_str.replace(',', ' ').split() if i.strip()]
    
    results = zxcvbn(password, user_inputs=user_inputs)
    
    score = results['score']
    crack_time = results['crack_times_display']['online_throttling_100_per_hour']

    strength_levels = {
        0: 'Terrible 🔴',
        1: 'Weak 🟠',
        2: 'Fair 🟡',
        3: 'Good 🟢',
        4: 'Strong 🟣'
    }

    output = []
    output.append(f"--- Analysis Results ---")
    output.append(f"Score (0-4): {score}")
    output.append(f"Strength: **{strength_levels.get(score, 'N/A')}**")
    output.append(f"Est. Crack Time (Online): {crack_time}")
    output.append(f"\nFeedback/Suggestions:")
    
    suggestions = results['feedback']['suggestions']
    if suggestions:
        for suggestion in suggestions:
            output.append(f"- {suggestion}")
    else:
        output.append("- None. Your password seems complex!")
    
    output.append(f"--------------------------")
    return "\n".join(output)

def generate_wordlist_logic(name, date_str, pet, year_range, output_file):
    """Core logic for wordlist generation."""
    
    base_words = set()
    if name:
        # Include case variations
        base_words.add(name.lower())
        base_words.add(name.capitalize())
        base_words.add(name.upper())
    if pet:
        # Include case variations
        base_words.add(pet.lower())
        base_words.add(pet.capitalize())
    
    date_parts = set()
    try:
        if date_str:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            year = str(date_obj.year)
            month = f"{date_obj.month:02}"
            day = f"{date_obj.day:02}"
            # Common date formats
            date_parts.update([year, year[2:], month, day, f"{month}{day}", f"{day}{month}", 
                               f"{month}{day}{year[2:]}", f"{day}{month}{year[2:]}", f"{year}{month}{day}"])
    except ValueError:
        return f"\n❌ Error: Could not parse date '{date_str}'. Use format YYYY-MM-DD."

    # 1. Leetspeak Generation
    wordlist = set(base_words)

    for word in base_words:
        char_options = [LEET_MAP.get(char, [char]) for char in word.lower()]
        leetspeak_permutations = [''.join(p) for p in product(*char_options)]
        wordlist.update(leetspeak_permutations)

    # 2. Append Years and Dates
    start_year = datetime.now().year - year_range
    end_year = datetime.now().year + 2 
    years = [str(y) for y in range(start_year, end_year)]
    
    final_wordlist = set(wordlist)
    for word in wordlist:
        for year in years:
            final_wordlist.add(word + year)
        for part in date_parts:
            final_wordlist.add(word + part)
    
    final_wordlist.update(date_parts)

    # 3. Export to .txt
    try:
        with open(output_file, 'w') as f:
            for word in sorted(list(final_wordlist)):
                f.write(word + '\n')
        
        return f"✅ Wordlist successfully generated!\nFile: **{output_file}**\nTotal unique words: **{len(final_wordlist)}**"
    except IOError as e:
        return f"❌ Error writing to file: {e}"

# --- Tkinter GUI Class ---

class PasswordToolGUI:
    def __init__(self, master):
        self.master = master
        master.title("🔐 Password Strength Analyzer & Wordlist Generator")
        master.geometry("650x550") # Set initial window size

        # Create notebook (tabs)
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")

        # Create frames for the tabs
        self.analyze_frame = ttk.Frame(self.notebook, padding="10")
        self.generate_frame = ttk.Frame(self.notebook, padding="10")

        # Add frames to the notebook
        self.notebook.add(self.analyze_frame, text="Password Analysis")
        self.notebook.add(self.generate_frame, text="Wordlist Generation")

        self.create_analyze_tab()
        self.create_generate_tab()

    def create_analyze_tab(self):
        """Builds the layout for the Password Analysis tab."""
        # 1. Password Input
        ttk.Label(self.analyze_frame, text="Enter Password:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.password_entry = ttk.Entry(self.analyze_frame, width=50, show="*")
        self.password_entry.grid(row=0, column=1, pady=5, padx=5)

        # 2. Toggle Visibility Button
        self.show_password = tk.BooleanVar()
        self.show_password.set(False)
        ttk.Checkbutton(self.analyze_frame, text="Show", variable=self.show_password, command=self.toggle_password_visibility).grid(row=0, column=2, padx=5)

        # 3. User Inputs (Context)
        ttk.Label(self.analyze_frame, text="User Inputs (Context - optional):").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.user_inputs_entry = ttk.Entry(self.analyze_frame, width=50)
        self.user_inputs_entry.grid(row=1, column=1, pady=5, padx=5)
        ttk.Label(self.analyze_frame, text="e.g., name, date, pet").grid(row=2, column=1, sticky="w", padx=5)

        # 4. Analyze Button
        ttk.Button(self.analyze_frame, text="Analyze Password", command=self.run_analysis).grid(row=3, column=0, columnspan=3, pady=15)

        # 5. Results Display
        ttk.Label(self.analyze_frame, text="Analysis Report:").grid(row=4, column=0, sticky="w", pady=5, padx=5)
        self.analysis_output = tk.Text(self.analyze_frame, height=15, width=65, state=tk.DISABLED, wrap=tk.WORD)
        self.analysis_output.grid(row=5, column=0, columnspan=3, pady=5, padx=5)
        
    def toggle_password_visibility(self):
        """Toggles the visibility of the password entry."""
        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def run_analysis(self):
        """Gets inputs and displays results in the Text widget."""
        password = self.password_entry.get()
        user_inputs_str = self.user_inputs_entry.get()
        
        report = analyze_password_logic(password, user_inputs_str)
        
        # Update Text widget
        self.analysis_output.config(state=tk.NORMAL)
        self.analysis_output.delete(1.0, tk.END)
        self.analysis_output.insert(tk.END, report)
        self.analysis_output.config(state=tk.DISABLED)

    def create_generate_tab(self):
        """Builds the layout for the Wordlist Generation tab."""
        
        # Common padding
        paddings = {'padx': 5, 'pady': 5}
        
        # 1. Name Input
        ttk.Label(self.generate_frame, text="Target Name:").grid(row=0, column=0, sticky="w", **paddings)
        self.name_entry = ttk.Entry(self.generate_frame, width=40)
        self.name_entry.grid(row=0, column=1, columnspan=2, sticky="ew", **paddings)

        # 2. Date Input
        ttk.Label(self.generate_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, sticky="w", **paddings)
        self.date_entry = ttk.Entry(self.generate_frame, width=40)
        self.date_entry.grid(row=1, column=1, columnspan=2, sticky="ew", **paddings)

        # 3. Pet Input
        ttk.Label(self.generate_frame, text="Pet Name:").grid(row=2, column=0, sticky="w", **paddings)
        self.pet_entry = ttk.Entry(self.generate_frame, width=40)
        self.pet_entry.grid(row=2, column=1, columnspan=2, sticky="ew", **paddings)

        # 4. Year Range
        ttk.Label(self.generate_frame, text="Years Back to Append:").grid(row=3, column=0, sticky="w", **paddings)
        self.year_range_spinbox = ttk.Spinbox(self.generate_frame, from_=5, to=50, increment=5, width=5)
        self.year_range_spinbox.set(10) # Default value
        self.year_range_spinbox.grid(row=3, column=1, sticky="w", **paddings)
        ttk.Label(self.generate_frame, text="e.g., 10 means last 10 years").grid(row=3, column=2, sticky="w", **paddings)
        
        # 5. Output File Selection
        self.output_path = tk.StringVar(value="wordlist_output.txt")
        ttk.Label(self.generate_frame, text="Output File:").grid(row=4, column=0, sticky="w", **paddings)
        ttk.Entry(self.generate_frame, textvariable=self.output_path, width=40).grid(row=4, column=1, sticky="ew", **paddings)
        ttk.Button(self.generate_frame, text="Browse", command=self.browse_output_file).grid(row=4, column=2, **paddings)

        # 6. Generate Button
        ttk.Button(self.generate_frame, text="Generate Wordlist & Export", command=self.run_generation).grid(row=5, column=0, columnspan=3, pady=15)

        # 7. Results Display
        ttk.Label(self.generate_frame, text="Generation Report:").grid(row=6, column=0, sticky="w", **paddings)
        self.generation_output = tk.Text(self.generate_frame, height=10, width=65, state=tk.DISABLED, wrap=tk.WORD)
        self.generation_output.grid(row=7, column=0, columnspan=3, pady=5, padx=5)

    def browse_output_file(self):
        """Opens a file dialog to select the output file path."""
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialfile=self.output_path.get()
        )
        if filename:
            self.output_path.set(filename)

    def run_generation(self):
        """Gathers inputs, runs the generation logic, and displays results."""
        name = self.name_entry.get().strip()
        date_str = self.date_entry.get().strip()
        pet = self.pet_entry.get().strip()
        output_file = self.output_path.get()
        
        try:
            year_range = int(self.year_range_spinbox.get())
        except ValueError:
            messagebox.showerror("Input Error", "Year Range must be a number.")
            return

        if not name and not date_str and not pet:
            messagebox.showwarning("Missing Input", "Please provide at least a Name, Date, or Pet Name for generation.")
            return
            
        report = generate_wordlist_logic(name, date_str, pet, year_range, output_file)
        
        # Update Text widget
        self.generation_output.config(state=tk.NORMAL)
        self.generation_output.delete(1.0, tk.END)
        self.generation_output.insert(tk.END, report)
        self.generation_output.config(state=tk.DISABLED)


if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordToolGUI(root)
    root.mainloop()

import tkinter as tk
from googletrans import Translator

class TextTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Translator")
        self.root.configure(bg="#E6E6FA")  # Lavender background color

        self.translator = Translator()

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(root, text="Text Translator", font=("Helvetica", 16, "bold"), bg="#E6E6FA")
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.source_lang_label = tk.Label(root, text="Source Language:", bg="#E6E6FA")
        self.source_lang_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.source_lang_entry = tk.Entry(root)
        self.source_lang_entry.grid(row=1, column=1, padx=10, pady=5)

        self.target_lang_label = tk.Label(root, text="Target Language:", bg="#E6E6FA")
        self.target_lang_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.target_lang_entry = tk.Entry(root)
        self.target_lang_entry.grid(row=2, column=1, padx=10, pady=5)

        self.text_label = tk.Label(root, text="Enter text to translate:", bg="#E6E6FA")
        self.text_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        self.text_entry = tk.Entry(root)
        self.text_entry.grid(row=3, column=1, padx=10, pady=5)

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text, bg="#9370DB", fg="white")
        self.translate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.translation_label = tk.Label(root, text="", wraplength=400, justify=tk.LEFT, bg="#E6E6FA")
        self.translation_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def translate_text(self):
        source_lang = self.source_lang_entry.get()
        target_lang = self.target_lang_entry.get()
        text = self.text_entry.get()

        if source_lang and target_lang and text:
            translated = self.translator.translate(text, src=source_lang, dest=target_lang)
            self.translation_label.config(text="Translated text:\n" + translated.text)
        else:
            self.translation_label.config(text="Please provide source, target language, and text")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextTranslatorApp(root)
    root.mainloop()

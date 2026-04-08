# 🧠 Marathi POS Tagging System (UPOS)

## 📌 Overview

This project is a **web-based NLP application** that performs Part-of-Speech (POS) tagging for Marathi and English using the Stanza NLP library.

It assigns **Universal POS (UPOS)** and **XPOS tags** to each word in real-time.

---

## 🚀 Tech Stack

* Python
* Stanza (Stanford NLP)
* Streamlit (Web UI)
* SQLite3 (Authentication Database)
* Pandas (Data Display)

---

## ✨ Features

* 🔤 Supports Marathi + English input
* 🧠 Automatic language detection (Unicode-based)
* 🔐 Login & Signup system
* 📊 Word-wise POS tagging (UPOS + XPOS)
* ⚡ Fast and interactive UI

---

## 🏗️ System Architecture

* Frontend: Streamlit Web App
* Backend: Stanza NLP Pipeline
* Database: SQLite (User authentication)

📎 Refer to PPT for detailed architecture diagram.

---

## 📊 Example

**Input:**

```
मी शाळेत जातो
```

**Output:**

| Word  | POS  | Detail |
| ----- | ---- | ------ |
| मी    | PRON | PRP    |
| शाळेत | NOUN | NN     |
| जातो  | VERB | VM     |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone repository

```bash
git clone https://github.com/your-username/marathi-pos-tagging
cd marathi-pos-tagging
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
streamlit run app.py
```

---

## 📎 Project Files

* 📄 NLP Project PPT included
* 💻 Full working Streamlit application
* 🗄️ SQLite database for authentication

---

## 📈 Results

* Accuracy: ~89%
* Precision: ~87%
* Recall: ~85%
* F1 Score: ~86%

📊 Based on evaluation using UD Marathi dataset.

---

## 💡 Innovation

* Bilingual POS tagging (Marathi + English)
* Automatic language detection
* Full-stack NLP web application
* User authentication system

---

## 📌 Future Scope

* Transformer-based models (BERT, BiLSTM)
* Support for more Indian languages
* Cloud deployment (AWS / GCP)

---

## 👨‍💻 Author

Harshal Ratan Kasar
23BCS053
IIIT Dharwad


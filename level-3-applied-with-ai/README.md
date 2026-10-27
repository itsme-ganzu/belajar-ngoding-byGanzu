# Level 3: Applied with AI (Engineering with LLM)

**Outcome:** Lu mampu memanfaatkan AI sebagai *pair programmer* cerdas untuk mempercepat penulisan kode tanpa menjadi bergantung, tidak tertipu halusinasi, dan menjaga standar keamanan software profesional.

---

## Modul Pembelajaran:
1. **[3.1: Anatomi & Batasan LLM dalam Koding](3.1-cara-kerja-llm/materi.md)**
   - Cara kerja token prediction, halusinasi library palsu, API usang, prinsip *Zero-Trust AI*.
2. **[3.2: Technical Specification & Context Prompting](3.2-spec-prompting/materi.md)**
   - Rumus R-C-I-E (*Role, Context, Instructions, Constraints*), mendikte batasan kode teknis ke LLM.
3. **[3.3: Code Review, Audit Keamanan, & Red Teaming AI](3.3-code-review-security/materi.md)**
   - Audit keamanan kebocoran API key (`.env`), pencegahan *hallucinated dependencies*, dan checklist review.

---

## 🏆 Gerbang Lulus Level 3: Ujian "Audit Bug AI"
Murid diberikan satu file kode buatan AI yang secara sengaja disisipi 3 jenis kelemahan:
1. Satu celah keamanan (SQL Injection atau Hardcoded Secret).
2. Satu bug halusinasi logika pada *boundary condition*.
3. Satu fungsi yang tidak efisien.

Tugas murid: Temukan ketiga masalah tersebut, jelaskan di mana letak bahayanya, tulis tes otomatis `pytest` yang menangkap kegagalan tersebut, dan perbaiki kodenya secara mandiri.

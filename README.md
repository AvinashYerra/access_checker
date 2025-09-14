
# Inspiration

While browsing the web, I realized how many websites are inaccessible to people with disabilities.  
Many accessibility issues like missing alt text, poor contrast, or improper ARIA usage are often overlooked by developers.  
I wanted to build an automated tool that helps developers and non-technical users easily check if their websites follow accessibility best practices.  
The open-source project [axe-core](https://www.deque.com/axe/) inspired me to leverage a powerful and standardized accessibility testing engine.

---

# What it does

Axess takes a website URL as input and performs an automated accessibility audit using Axe.  
It scans the page in a headless browser, collects accessibility violations, and presents them in an interactive table.  
Users can also download a detailed CSV report of the issues found.

---

# How we built it

- Built the frontend using **Streamlit** for fast and interactive UI development.
- Automated browser interaction using **Selenium WebDriver**.
- Integrated **axe_selenium_python** to run axe-core accessibility scans.
- Used **pandas** to manage data and enable CSV export.
- Handled deployment on **Streamlit Community Cloud** with appropriate system binaries for compatibility.

---

# What's next for Axess

- Add support for scanning multiple pages in a single run.
- Provide automated suggestions and fixes for common accessibility problems.
- Implement historical comparison of audit reports to track progress.
- Add more export options such as JSON and PDF.
- Build a visual dashboard to track accessibility trends over time.

🚀 Axess is our step toward a more inclusive web.

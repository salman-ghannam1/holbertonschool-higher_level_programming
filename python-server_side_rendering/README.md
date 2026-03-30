# Server-Side Rendering with Flask and Jinja

## Overview

This project demonstrates how to build dynamic web pages using **Server-Side Rendering (SSR)** with **Python**, **Flask**, and the **Jinja templating engine**.

In server-side rendering, the server generates the HTML content before sending it to the browser. This approach improves initial page load performance, enhances SEO, and reduces the amount of JavaScript required on the client side.

---

## Objectives

The main goals of this project are:

- Understand the concept of **server-side rendering**
- Learn the difference between **SSR** and **client-side rendering (CSR)**
- Build dynamic web pages using **Flask**
- Use **Jinja templates** to inject data into HTML
- Read and display data from different sources such as:
  - JSON files
  - CSV files
  - SQLite databases
- Handle dynamic content and user input efficiently

---

## What is Server-Side Rendering?

Server-side rendering is a technique where the server processes data and generates a complete HTML page before sending it to the client.

### Example:

Instead of sending an empty page and using JavaScript to fill it later, the server sends ready-to-display HTML.

This means:

- Faster first content display
- Better support for search engines
- Less dependency on client-side JavaScript

---

## SSR vs CSR

| Feature               | Server-Side Rendering (SSR) | Client-Side Rendering (CSR) |
| --------------------- | --------------------------- | --------------------------- |
| HTML generation       | On the server               | In the browser              |
| Initial load speed    | Faster                      | Slower                      |
| SEO support           | Better                      | Weaker                      |
| JavaScript dependency | Lower                       | Higher                      |
| Server load           | Higher                      | Lower                       |

---

## Why Server-Side Rendering is Important

Server-side rendering is useful because it:

- Improves **SEO**
- Delivers content faster on initial page load
- Makes applications more accessible in low-JavaScript environments
- Reduces client-side complexity
- Works well for content-driven websites and dashboards with moderate interaction

---

## Technologies Used

- **Python 3**
- **Flask**
- **Jinja2**
- **HTML5**
- **CSS3**
- **JSON**
- **CSV**
- **SQLite**

---

## Project Structure

```bash
project/
│── app.py
│── templates/
│   │── index.html
│   │── users.html
│   │── products.html
│── static/
│   │── style.css
│── data/
│   │── users.json
│   │── products.csv
│   │── database.db
│── README.md
```

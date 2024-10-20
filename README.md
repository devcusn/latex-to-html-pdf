# LaTeX to HTML/PDF Converter with Pandoc

This project is a Flask application that converts LaTeX documents into HTML and PDF formats. Users can interact with the LaTeX file and view the results of the conversion.

## Project Structure

```
-static
     -style.css
-views
    index.html
    pdf.html
app.py
Dockerfile
docker-compose.yaml
file.tex
```

### Files

- `app.py`: The main file of the Flask application.
- `Dockerfile`: The file used to build the Docker image of the application.
- `docker-compose.yaml`: The configuration file used to manage Docker containers.
- `file.tex`: The LaTeX file to be converted.
- `views/index.html`: The homepage.
- `views/pdf.html`: The PDF viewing page.
- `static/style.css`: The stylesheet.

## Requirements

To run this project, the following software must be installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Pandoc](https://pandoc.org/)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/devcusn/latex-to-html-pdf.git
   cd latex-to-html-pdf
   ```

## Usage

### Running with Docker

1. Make sure Docker and Docker Compose are installed.
2. Start the application with the following command:
   ```bash
   docker-compose up
   ```
3. Open your browser and go to `http://localhost:4003`.
4. Open your browser and go to `http://localhost:4003/pdf`.

### API Usage

- **To Get the HTML Report:**

  - `GET /api/v1/get-report`
  - Returns: The LaTeX file converted into HTML format.

- **To Get the PDF Report:**
  - `GET /api/v1/get-pdf`
  - Returns: The LaTeX file converted into PDF format.

## Contributing

Contributions are always welcome! Feel free to suggest changes or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

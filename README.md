# Codemob

Codemob is a web application designed to combine the features of a Q&A forum and a tutorial platform. Users can ask questions, watch video tutorials, and interact with mentors to enhance their learning experience. The app is built using Django, Bootstrap, jQuery, and AJAX.

## Features

- **Forum:** Users can ask questions and get answers, similar to Stack Overflow.
- **Tutorials:** Video tutorials from mentors on specific topics, with the ability to comment and ask for assistance.
- **Search:** Find related video tutorials, forum questions, mentors, and other accounts.
- **Tags:** Videos and questions can be tagged for easy categorization and searchability.
- **Follow Mentors:** Follow mentors who specialize in specific topics to stay updated with their content.
- **Private Messaging:** Send private messages to mentors for follow-up assistance.

## Technology Stack

- **Backend:** Django
- **Frontend:** Bootstrap, jQuery, AJAX

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/AnesuMugiya/Codemob.git
    cd degee
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

6. **Access the application:**

    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### Forum

- Post questions on various topics.
- Provide answers to questions posted by others.
- Tag questions for easy searching and categorization.

### Tutorials

- Watch video tutorials from mentors on specific topics.
- Comment on videos to ask questions and get assistance.
- Follow mentors to stay updated with their latest tutorials.
- Send private messages to mentors for more personalized assistance.

### Search

- Use the search feature to find video tutorials, forum questions, mentors, and other user accounts.
- Utilize tags to narrow down search results.

## Contributing

1. **Fork the repository:**

    ```sh
    git fork https://github.com/AnesuMugiya/degee.git
    ```

2. **Create a new branch:**

    ```sh
    git checkout -b feature/your-feature-name
    ```

3. **Make your changes and commit them:**

    ```sh
    git commit -m "Add your feature"
    ```

4. **Push to the branch:**

    ```sh
    git push origin feature/your-feature-name
    ```

5. **Create a Pull Request:**

    Go to the repository on GitHub and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to open an issue or contact me!

---

Thank you for checking out Degee!

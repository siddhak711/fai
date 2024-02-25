// autocomplete.js

document.addEventListener('DOMContentLoaded', function() {
    const chapters = document.querySelectorAll('.chapter-card');
    const inputBox = document.getElementById('input-box');

    inputBox.addEventListener('input', function() {
        const input = inputBox.value.trim().toLowerCase();

        chapters.forEach(chapter => {
            const chapterName = chapter.querySelector('.chapter-name').textContent.toLowerCase();
            if (input === '' || chapterName.includes(input)) {
                chapter.style.display = 'block';
            } else {
                chapter.style.display = 'none';
            }
        });
    });
});

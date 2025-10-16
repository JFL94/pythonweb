document.addEventListener("DOMContentLoaded", function () {
    //選取元素
    const toggleButton = document.querySelector('.toggle-button');
    const answerContent = document.querySelector('.answer-content');

    toggleButton.addEventListener('click', function () {
        // 切換 visible class
        answerContent.classList.toggle('visible');
    });

});
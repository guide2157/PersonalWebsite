
    var changeLanguageForm = document.getElementById("languageForm");
    var changeLanguageInput = document.getElementById("languageInput");
    var languages = document.querySelectorAll("#language");
    for (var i = 0; i < languages.length; i++) {
    language[i].addEventListener('click', submitForm);
}
    function submitForm(){
    changeLanguageInput.setAttribute("value",this.name);
        changeLanguageForm.submit();
}
odoo.define('digizilla.hide_create_button', [], function (require) {
    'use strict';

    const callback = () => {
        const createButtons = document.querySelectorAll('.o_form_button_create');
        createButtons.forEach(button => {
            button.style.display = 'none';
        });
    };

    callback();
    const mutationObserver = new MutationObserver(callback);
    mutationObserver.observe(document, {subtree: true, childList: true});
});

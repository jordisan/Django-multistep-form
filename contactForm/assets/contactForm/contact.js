// global namespace
var general = general || {};

// module for contact form
general.ContactForm = (function(){
    'use strict';

    var _container = null;

    /**
     * Update form data from API using email
     * TODO: obvious privacy issues here
     * @param {*} email 
     */
    function _updateCustomerData(email) {
        general.API.getCustomerData(email).then(function(data) {
            if (!!data) {
                _container.querySelector('#id_first_name').value=data.first_name;
                _container.querySelector('#id_last_name').value=data.last_name;
                _container.querySelector('#id_phone_number').value=data.phone_number;
            }
        });
    }

    /**
     * Initialize contact form
     * @param {*} container 
     */
    function _init(container) {
        _container = container;
        if (!! _container) {
            // attach listener to email field to get data from API
            var email_field = _container.querySelector('#id_email');
            if (!! email_field) {
                email_field.addEventListener('blur', function(e) {
                    _updateCustomerData(e.target.value);
                });
            }
        }
    };

    return {
        init: _init
    };
})();

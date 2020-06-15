// module for contact form
var contactForm = (function(){
    var container = null;

    function getCustomerData(email) {
        var me = this;
        if (!!email) {
            fetch('/api/customers/' + encodeURIComponent(email))
            .then(function(response) {
                console.log(response);
            })
            .catch(function(err) {
                console.log(err);
            })
        }
    };

    function init(container) {
        this.container = container;
        if (!!container) {
            // attach listener to email field to get data from API
            container.querySelector('#id_email').addEventListener('blur', function(e) {
                getCustomerData(e.target.value);
            });
        }
    };

    return {
        init: init
    };
})();

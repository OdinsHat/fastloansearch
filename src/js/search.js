(function ($) {
    'use strict';

    function runSearch() {
        var formdata = $('#frm-quick-search').serialize();
        var url = $('#frm-quick-search')[0].action;
        $.ajax({
            dataType: "json",
            url: url,
            data: formdata,
            success: returnResults
        });
        return false;
    }

    function recursiveResult(key, val){
        console.log(key);
        console.log(val);
    }

    $(function($) {
        $('#loan-unsecured').addClass('animated bounceInLeft');
        $('#loan-secured').addClass('animated bounceInDown');
        $('#loan-badcredit').addClass('animated bounceInRight');

        $('#loan-car').addClass('animated bounceInLeft');
        $('#loan-holiday').addClass('animated bounceInUp');
        $('#loan-wedding').addClass('animated bounceInRight');

        $('div.loans-row div h4').fadeIn(3000);
    });
}($));

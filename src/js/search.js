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
        $('#loans-icon').addClass('animated bounceInLeft');
        $('#card-icon').addClass('animated bounceInDown');
        $('#home-icon').addClass('animated bounceInRight');
    });

    
}($));

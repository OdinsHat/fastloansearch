(function ($) {
    'use strict';
    /**
     * Created by doug on 21/03/2014.
     */

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

    function returnResults(data) {
        var resultitems = data.items;
        $.each(resultitems, function(k, v){
            recursiveResult(k, v);
        });

        /*
        var resulthtml = '';
        var count = resultitems.length;
        for (i = 0; i < count; i++) {
            resulthtml += '<article class="result-' + i + '" style="opacity:0">';
            resulthtml += '<h3><a hrf="' + resultitems[i].link + '">' + resultitems[i].title + '</a></h3>';
            resulthtml += '<p>' + resultitems[i].snippet + '</p>';
            resulthtml += '<small>' + resultitems[i].displayLink + '</small>';
            resulthtml += '</article>';
            $('#results').append(resulthtml);
            $('.result-' + i).addClass('animated bounceInUp');
            resulthtml = '';
        }
        */
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

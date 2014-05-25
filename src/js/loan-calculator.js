BorrowingCosts = (function() {

    /**
     * Given any value and should return a float or false
     *
     * @param value
     * @returns {*}
     */
    var getCleanFloat = function(value){
        var cleanedFloat = parseFloat(borrowAmt.replace(/[^0-9.]/g, ''));
        if(!isNaN(cleanedFloat) && cleanedFloat > 0){
            return cleanedFloat;
        }
        return false;
    };

    /**
     * Given monthly rate and termMonths return the multiplier
     * @param monthlyRate
     * @param termMonths
     */
    var calculateMultiplier = function(monthlyRate, termMonths){
        var multiplier;
        multiplier = 1 + monthlyRate;
        multiplier = Math.pow(multiplier, termMonths);
        multiplier = 1 - multiplier;
        multiplier = monthlyRate / multiplier;
        return multiplier;
    };

    return {
        loanCost: function(loan, apr, term){
            var monthlyRate = apr/1200;
            var termMonths = term * -1;
            var multiplier = calculateMultiplier(monthlyRate, termMonths);
            var monthlyRepayments = loan * multiplier;
            return monthlyRepayments * term - loan;
        },
        monthlyRepayments: function(loan, apr, term){
            var monthlyRate = apr/1200;
            var termMonths = term * -1;
            var multiplier = calculateMultiplier(monthlyRate, termMonths);
            var monthlyRepayments = loan * multiplier;
            return monthlyRepayments;
        }
    };


}());

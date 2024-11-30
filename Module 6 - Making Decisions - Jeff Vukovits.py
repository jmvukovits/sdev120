start

Declarations
    num baseFee = 5
    num textFee100 = 100 * .03
    num textFee300 = .02
    num taxRate = 14%

    input customerAreaCode = "XXX"
    input customerNumber = "XXX-XXXX"
    input textAmount = "the number of texts this month"
        while textAmount > 100 then
            textOverLimit()
        endwhile
    baseFee + textCharge = preTaxBill
    preTaxBill * taxRate = taxCharge
    preTaxBill + taxCharge = billTotal
        if textAmount > 100
            output "You're text messages exceeds 100 texts this month"
            if billTotal > 10
                output "Your bill exceeds $10 this month"
            endif
        endif
    output " Your bill before taxes is preTaxBill"
    output "Your bill after taxes is billTotal"
stop

        textOverLimit()
            if textAmount > 100
                if textAmount < 300 then
                    (textAmount - 100) * .03 = textCharge
                    if textAmount > 300 then
                        (textAmount - 300) * textFee300 + textFee100 = textCharge
                    else textCharge = 0
                    endif
                endif
            endif
            return

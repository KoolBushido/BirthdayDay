#lang racket
;Racket version of the program
;@author Jonathan Hsin
;@date 7/14/2024

;function to check if a year is a leap year
(define (is-leap year)
    (cond
        ((null? year) #f)
        ((= (remainder year 4) 0) (cond 
            ((= (remainder year 100) 0)(cond
                ((= (remainder year 400) 0) #t)
                (else #f)
                ))
            (else #t))
        )
        (else #f)
    )
)
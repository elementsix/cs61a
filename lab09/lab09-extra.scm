(define (composed f g)
  (lambda (x) (f (g x)))
)

(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  'YOUR CODE HERE
)

(define (filter f lst)
  (cond ((null? lst) nil)
        ((f (car lst)) (cons (car lst) (filter f (cdr lst))))
        (else (filter f (cdr lst)))
  )
)

(define (all-satisfies lst pred)
  (equal? (length (filter pred lst)) (length lst))
)

(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (accumulate combiner (combiner start (term n)) (- n 1) term)
  )
)


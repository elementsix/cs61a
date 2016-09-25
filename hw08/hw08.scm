(define (deep-map fn s)
  ; YOUR-CODE-HERE
  (cond ((null? s) s)
        ((or (number? (car s)) (symbol? (car s))) (cons (fn (car s)) (deep-map fn (cdr s))))
        ((pair? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
  )
)

(define (substitute s old new)
  ; YOUR-CODE-HERE
  ; How to do this by reusing deep-map?
  (cond ((null? s) s)
        ((and (or (number? (car s)) (symbol? (car s))) (equal? (car s) old))       (cons new (substitute (cdr s) old new)))
        ((and (or (number? (car s)) (symbol? (car s))) (not (equal? (car s) old))) (cons (car s) (substitute (cdr s) old new)))
        ((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
  )
)

(define (sub-all s olds news)
  ; YOUR-CODE-HERE
  (cond ((or (null? s) (null? olds) (null? news)) s)
        ((not (null? (cdr olds))) (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
        ((null? (cdr olds)) (substitute s (car olds) (car news)))
  )
)



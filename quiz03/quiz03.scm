; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

(define (map f s)
  ; List the result of applying f to each element in s.
  (if (null? s) s
    (cons (f (car s)) (map f (cdr s)))))

(define (filter f s)
  ; List the elements of s for which f returns a true value.
  (if (null? s) s
    (let ((rest (filter f (cdr s))))
      (if (f (car s)) (cons (car s) rest) rest))))

(define (no-repeats s)
  ; YOUR-CODE-HERE
  (if (null? s) s
    (let ((f (lambda (x) (not (equal? (car s) x)))))
      (cons (car s) (filter f (no-repeats (cdr s)))))
  )
)

(define (how-many-dots s)
  ; YOUR-CODE-HERE
  (cond ((null? s) 0)        
        ((and (pair? s) (number? (car s)) (number? (cdr s))) 1)
        ((and (pair? s) (pair? (car s)) (pair? (cdr s))) (+ (how-many-dots (car s)) (how-many-dots (cdr s))))
        ((and (pair? s) (number? (car s)) (pair? (cdr s))) (how-many-dots (cdr s)))
        ((and (pair? s) (pair? (car s)) (number? (cdr s))) (+ 1 (how-many-dots (car s))))
        ((and (pair? s) (pair? (car s)) (null? (cdr s))) (how-many-dots (car s)))
        (else 0)
  )
)

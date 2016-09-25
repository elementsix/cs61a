(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (cadr (cdr s))
)

(define (sign x)
  (cond ((< x 0) -1)
        ((> x 0) 1)
        (else 0)
  )
)

(define (square x) (* x x))

(define (pow b n)
  (cond ((equal? n 0) 1)
        ((odd? n) (* b (pow b (- n 1))))
        ((even? n) (pow (square b) (/ n 2)))
  )
)

(define (ordered? s)
  (cond ((or (null? s) (null? (cdr s))) #t)
        ((<= (car s) (cadr s)) (ordered? (cdr s)))
        (else #f)
  )
)

(define (nodots s)
  (cond ((null? s) nil)
        ((number? s) (cons s nil))
        ((number? (car s)) (cons (car s) (nodots (cdr s))))
        (else (cons (nodots (car s)) (nodots (cdr s))))
  )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((> (car s) v) false)
          ((equal? (car s) v) true)
          (else (contains? (cdr s) v))
    )
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((equal? (car s) v) s)
          ((> (car s) v) (cons v s))
          (else (cons (car s) (add (cdr s) v)))
    )
)

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((equal? (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          (else (intersect s (cdr t)))
    )
)

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((contains? s (car t)) (union s (cdr t)))
          (else (union (add s (car t)) (cdr t)))
    )
)


; Binary search trees

; A data abstraction for binary trees where nil represents the empty tree
(define (tree entry left right) (list entry left right))
(define (entry t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf entry) (tree entry nil nil))

(define (in? t v)
    (cond ((empty? t) false)
          ((equal? (car t) v) true)
          ((< (car t) v) (in? (right t) v))
          (else (in? (left t) v))
    )
)

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.entry == v:
;         return True
;     elif s.entry < v:
;         return contains(s.right, v)
;     elif s.entry > v:
;         return contains(s.left, v)

(define (as-list t)
    
    (else nil)
)


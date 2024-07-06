

(define (problem BW-rand-4)
(:domain blocksworld-4ops)
(:objects object_0 object_1 object_2 object_3 )
(:init
(ontable object_0)
(ontable object_3)
(clear object_0)
(clear object_3)
(clear object_1)
(ontable object_1)
(holding object_2)
)
(:goal
(and
(on object_2 object_1))
)
)

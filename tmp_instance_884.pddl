

(define (problem BW-rand-4)
(:domain blocksworld-4ops)
(:objects object_0 object_1 object_2 object_3 )
(:init
(clear object_0)
(ontable object_0)
(ontable object_3)
(clear object_2)
(on object_2 object_3)
(holding object_1)
)
(:goal
(and
(on object_1 object_2)
(on object_2 object_3))
)
)



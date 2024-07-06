

(define (problem BW-rand-4)
(:domain blocksworld-4ops)
(:objects object_0 object_1 object_2 object_3 )
(:init
(ontable object_2)
(on object_3 object_2)
(clear object_1)
(on object_1 object_3)
(holding object_0)
)
(:goal
(and
(on object_0 object_1)
(on object_1 object_3)
(on object_3 object_2))
)
)



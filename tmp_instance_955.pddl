

(define (problem BW-rand-4)
(:domain blocksworld-4ops)
(:objects object_0 object_1 object_2 object_3 )
(:init
(ontable object_2)
(ontable object_0)
(clear object_3)
(on object_3 object_0)
(holding object_1)
(clear object_2)
)
(:goal
(and
(on object_1 object_3)
(on object_3 object_0))
)
)





(define (problem BW-rand-4)
(:domain blocksworld-4ops)
(:objects object_0 object_1 object_2 object_3 )
(:init
(ontable object_3)
(ontable object_2)
(clear object_0)
(on object_0 object_2)
(holding object_1)
(clear object_3)
)
(:goal
(and
(on object_0 object_2)
(on object_1 object_0))
)
)



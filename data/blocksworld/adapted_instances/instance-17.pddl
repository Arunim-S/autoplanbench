

(define (problem BW-rand-4)
(:domain blocksworld-4ops)
(:objects object_0 object_1 object_2 object_3 )
(:init
(handempty)
(on object_0 object_3)
(ontable object_1)
(ontable object_2)
(on object_3 object_2)
(clear object_0)
(clear object_1)
)
(:goal
(and
(on object_1 object_2)
(on object_2 object_3))
)
)



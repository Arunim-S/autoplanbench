

(define (problem BW-rand-4)
(:domain blocksworld-4ops)
(:objects object_0 object_1 object_2 object_3 )
(:init
(ontable object_0)
(ontable object_3)
(clear object_2)
(on object_2 object_3)
(handempty)
(clear object_1)
(on object_1 object_0)
)
(:goal
(and
(on object_1 object_0)
(on object_2 object_3)
(on object_3 object_1))
)
)





(define (problem BW-rand-4)
(:domain blocksworld-4ops)
(:objects object_0 object_1 object_2 object_3 )
(:init
(ontable object_1)
(clear object_3)
(ontable object_3)
(clear object_0)
(ontable object_0)
(clear object_1)
(clear object_2)
(handempty)
(ontable object_2)
)
(:goal
(and
(on object_0 object_3)
(on object_3 object_1))
)
)



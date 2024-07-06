(define (problem blocksworld-problem)
   (:domain rohit)
 
  (:objects
 	A
 	B
 	C
   )
   (:init
 	(block-clear A)
 	(block-clear B)
 	(block-clear C)
 	(block-on-table A)
 	(block-on-table B)
 	(block-on-table C)
 	(robot-hand-empty)
   )
   (:goal
 	(and
   	(block-on A B)
   	(block-on B C)
   	(block-on-table C)
 	)
   )
 )

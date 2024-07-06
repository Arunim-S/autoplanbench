(define (domain rohit)
(:requirements :typing)
(:predicates
  (block-clear ?x - block)
  (block-on-table ?x - block)
  (robot-hand-empty)
  (robot-holding ?x - block)
  (block-on ?x - block ?y - block)
)
(:action dance
  :parameters(
    ?x - block
  )
  :precondition(and
  (block-clear ?x)
  (block-on-table ?x)
  (robot-hand-empty)
)
  :effect(and
  (not (block-on-table ?x))
  (not (block-clear ?x))
  (robot-holding ?x)
  (forall (?y - block) (when (block-on ?y ?x) (block-clear ?y) ) )
  (robot-hand-empty)
)

)(:action sing
  :parameters(
    ?x - block
  )
  :precondition(and
  (robot-holding ?x)
)
  :effect(and
  (not (robot-holding ?x))
  (block-clear ?x)
  (robot-hand-empty)
  (block-on-table ?x)
)

)(:action jump
  :parameters(
    ?x - block
    ?y - block
  )
  :precondition(and
  (robot-holding ?x)
  (block-clear ?y)
)
  :effect(and
  (not (robot-holding ?x))
  (not (block-clear ?y))
  (robot-hand-empty)
  (block-on ?x ?y)
  (block-clear ?x)
)

)(:action rama
  :parameters(
    ?x - block
    ?y - block
  )
  :precondition(and
  (block-clear ?x)
  (block-on ?x ?y)
  (robot-hand-empty)
)
  :effect(and
  (not (block-on ?x ?y))
  (not (robot-hand-empty))
  (robot-holding ?x)
  (block-clear ?y)
)

)
)
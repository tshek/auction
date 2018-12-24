items = [
  # [item_number, description, reserve_price,
  #   [ [bid, buyer], 
  #     [bid, buyer], 
  #     [bid, buyer] 
  #   ] 
  # ]
    
  [ 101, "Chest of drawers", 199.99, 
    [
        [0, None]
    ]
  ],
    
  [ 102, "Cuddly toy", 5.00, 
    [
        [0, None]   
    ] 
  ],
    
  [ 103, "Armchair", 25.00, 
    [
        [0, None] 
    ]
  ],
    
  [ 104, "Hair brush used by pop celebrity Ed Sheeran", 20.00,
    [
      [0, None]
    ]
  ]
]

'''

# Task 2 – Buyer bids.

A buyer should be able to find an item and view the item number, description and the current highest
bid. A buyer can then enter their buyer number and bid, which must be higher than any previously
recorded bids. Every time a new bid is recorded the number of bids for that item is increased by one.
Buyers can bid for an item many times and they can bid for many items.


Transcript                                        # notes

==============
Items for Sale
==============

Lot 101: "Chest of drawers". Highest bid: $130
Lot 102: "Cuddly toy". Highest bid: $5.00
Lot 103: "Armchair". Highest bid: $18.00
Lot 104: Hair brush used by pop celebrity Ed Sheeran: $0.00


Select a lot to bid on: 101

Highest bid on "Chest of drawers" (#101) is $130.00
Enter your bid (or press ENTER to cancel): $ 120      # too low (fail)

Sorry, your bid must exceed $130
Enter your bid (or press ENTER to cancel): $ 130      # same bid (fail)

Sorry, your bid must exceed $130
Enter your bid (or press ENTER to cancel): $          # cancelled 
Bid cancelled

==============
Items for Sale
==============

Lot 101: Chest of drawers. Highest bid: $130.00
Lot 102: Cuddly toy. Highest bid: $5.00
Lot 103: Armchair. Highest bid: $18.00
Lot 104: Hair brush used by pop celebrity Ed Sheeran: $20.00


Select a lot to bid on: 101

Highest bid on "Chest of drawers" (#101) is $130.00
Enter your bid (or press ENTER to cancel): $ 140
Bid accepted. 

Enter your buyer number: 444444
Bid confirmed, $140 on "Chest of drawers" for buyer 444444

==============
Items for Sale
==============

Lot 101: Chest of drawers. Highest bid: $140
Lot 102: Cuddly toy. Highest bid: $5.00
Lot 103: Armchair. Highest bid: $18.00
Lot 104: Hair brush used by pop celebrity Ed Sheeran: $0.00

'''

'''
State of items variable BEFORE Transcript session:

items = [

  [ 101, "Chest of drawers", 199.99, 
    [ 
      [0, None], 
      [50.00, 111111], 
      [100.00, 222222], 
      [130.00, 111111] 
     ] 
  ],
    
  [ 102, "Cuddly toy", 5.00, 
    [ 
      [0, None], 
      [ 2.00, 444444], 
      [5.00, 111111]                    
    ] 
  ],
    
  [ 103, "Armchair", 25.00, 
    [ 
      [0, None], 
      [18.00, 333333]
    ] 
  ],
    
  [ 104, "Hair brush used by pop celebrity Ed Sheeran", 20.00,
    [ # bids
      [0, None]
    ]
  ]
] # end of items



State of items variable AFTER Transcript session:


items = [
  
  [ 101, "Chest of drawers", 199.99, 
    [ 
      [0, None], 
      [50.00, 111111], 
      [100.00, 222222], 
      [130.00, 111111],
      [140.00, 444444]
     ] 
  ],
    
  [ 102, "Cuddly toy", 5.00, 
    [ 
      [0, None], 
      [ 2.00, 444444], 
      [5.00, 111111]                    
    ] 
  ],
    
  [ 103, "Armchair", 25.00, 
    [ 
      [0, None], 
      [18.00, 333333]
    ] 
  ],
    
  [ 104, "Hair brush used by pop celebrity Ed Sheeran", 20.00,
    [ # bids
      [0, None]
    ]
  ]
] # end of items


'''
def banner (text, ornament="="):
  above = below = ornament * len(text)
  return f"{above}\n{text}\n{below}"

def display_catalog():
  print (banner ("Items for sale") )
  texts = []
  for item in items:
    lot, desc, reserve, bids = item
    texts.append (f"Lot {lot}: {desc}. Highest bid: ${bids[-1][0]}")
  print ("\n".join(texts))
    

display_catalog()

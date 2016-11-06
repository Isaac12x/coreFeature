//
//  Personality+JSON.swift
//  TextAnalysis
//
//  Created by Isaac Albets Ramonet on 06/11/2016.
//  Copyright © 2016 isaacalbetsramonet. All rights reserved.
//

import Arrow

extension User: ArrowParsable {
    
    mutating func deserialize(_ json: JSON) {
        name <-- json["tree.children.children.children.children.name"]
        percentage <-- json["tree.children.children.children.children.percentage"]
    }
}

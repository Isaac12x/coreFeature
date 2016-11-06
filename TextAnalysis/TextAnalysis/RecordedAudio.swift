//
//  Recorded.swift
//  TextAnalysis
//
//  Created by Isaac Albets Ramonet on 06/11/2016.
//  Copyright © 2016 isaacalbetsramonet. All rights reserved.
//

import Foundation

class RecordedAudio{
    
    var filePathUrl: NSURL!
    var title: String!
    
    init(filePathUrl: NSURL, title: String){
        self.filePathUrl = filePathUrl
        self.title = title
    }
}

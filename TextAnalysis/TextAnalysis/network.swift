//
//  network.swift
//  TextAnalysis
//
//  Created by Isaac Albets Ramonet on 06/11/2016.
//  Copyright © 2016 isaacalbetsramonet. All rights reserved.
//

import UIKit



struct Network {
    static func getJSONData() -> [[String:AnyObject]] {
        let path = Bundle.main.path(forResource: "activities", ofType: "json")
        let jsonData = NSData(contentsOfFile: path!)
        do
        {
            let jsonArray = try JSONSerialization.jsonObject(with: jsonData! as Data, options: .mutableContainers) as! [String:AnyObject]
            
            return jsonArray["activities"] as!  [[String:AnyObject]]
        }
        catch{}
        
        return [[String:AnyObject]]()
    }
}

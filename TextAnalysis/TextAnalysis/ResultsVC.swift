//
//  ResultsVC.swift
//  TextAnalysis
//
//  Created by Isaac Albets Ramonet on 06/11/2016.
//  Copyright © 2016 isaacalbetsramonet. All rights reserved.
//

import UIKit
import Alamofire

class ResultsVC: UIViewController{

    @IBOutlet weak var activityView: UIActivityIndicatorView!
    @IBOutlet weak var positive: UILabel!
    @IBOutlet weak var openess: UILabel!
    @IBOutlet weak var conscientiousness: UILabel!
    @IBOutlet weak var extraversion: UILabel!
    @IBOutlet weak var agreeableness: UILabel!
    @IBOutlet weak var neuroticism: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        activityView.startAnimating()
        activityView.isHidden = false
    }
    
    
    func get_response(){
    }
    
    func configurateForDisplay(){
        positive.text = "0.9"
        openess.text = "0.2"
        conscientiousness.text = "0.3"
        extraversion.text = "0.3"
        agreeableness.text = "0.5"
        neuroticism.text = "0.6"
    }
    
}

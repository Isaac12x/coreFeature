//
//  ViewController.swift
//  TextAnalysis
//
//  Created by Isaac Albets Ramonet on 05/11/2016.
//  Copyright © 2016 isaacalbetsramonet. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var tapRecognizer: UITapGestureRecognizer? = nil
    var keyboardAdjusted = false
    var lastKeyboardOffset : CGFloat = 0.0
    
    //MARK: UIViewController lifecycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        self.subscribeToKeyboardNotifications()
        self.addKeyboardDismissRecognizer()
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        self.unsubscribeFromKeyboardNotifications()
        self.removeKeyboardDismissRecognizer()
        
    }
    
    //KEYBOARD
        
        
        func addKeyboardDismissRecognizer() {
            self.view.addGestureRecognizer(tapRecognizer!)
        }
        
        func removeKeyboardDismissRecognizer() {
            self.view.removeGestureRecognizer(tapRecognizer!)
        }
        
        func handleSingleTap(recognizer: UITapGestureRecognizer) {
            self.view.endEditing(true)
        }
        
        func subscribeToKeyboardNotifications() {
            NotificationCenter.default.addObserver(self, selector: Selector(("keyboardWillShow:")), name: NSNotification.Name.UIKeyboardWillShow, object: nil)
            NotificationCenter.default.addObserver(self, selector: Selector(("keyboardWillHide:")), name: NSNotification.Name.UIKeyboardWillHide, object: nil)
        }
        
        func unsubscribeFromKeyboardNotifications() {
            NotificationCenter.default.removeObserver(self, name: NSNotification.Name.UIKeyboardWillShow, object: nil)
        }
    
        func keyboardWillShow(notification: NotificationCenter) {
            
            if keyboardAdjusted == false {
                lastKeyboardOffset = getKeyboardHeight(notification) / 2
                self.view.superview?.frame.origin.y -= lastKeyboardOffset
                keyboardAdjusted = true
            }
        }
        
        func keyboardWillHide(notification: NSNotification) {
            
            if keyboardAdjusted == true {
                self.view.superview?.frame.origin.y += lastKeyboardOffset
                keyboardAdjusted = false
            }
        }
        
        func getKeyboardHeight(notification: NSNotification) -> CGFloat {
            let userInfo = notification.userInfo
            let keyboardSize = userInfo![UIKeyboardFrameEndUserInfoKey] as! NSValue // of CGRect
            return keyboardSize.cgRectValue.height
        }
        
    
    

}


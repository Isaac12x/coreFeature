//
//  RecordAudio.swift
//  TextAnalysis
//
//  Created by Isaac Albets Ramonet on 06/11/2016.
//  Copyright © 2016 isaacalbetsramonet. All rights reserved.
//

import Foundation
import Alamofire
import UIKit
import AVFoundation

class RecordSoundsVC: UIViewController, AVAudioRecorderDelegate {
    
    // Variable declaration
    
    @IBOutlet weak var recordButton: UIButton!
    
    @IBOutlet weak var tapToRecord: UILabel!
    
    @IBOutlet weak var stopButton: UIButton!
    
    // Variables Declared Globally
    
    var audioRecorder: AVAudioRecorder!
    var recordedAudio: RecordedAudio!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    override func viewWillAppear(_ animated: Bool) {
        stopButton.isHidden = true
        tapToRecord.isHidden = false
        tapToRecord.text = "Tap to record"
    }
    
    // Prepare buttons to be displayed then locate the
    // main directory of the app, declare the name of the
    // recording pass it to an array then to a filePath
    // so we can track it. Initialitzate a session of
    // audio and then start audioRecorder passing the
    // path to the file and performing the recording.
    
    @IBAction func recordAudio(sender: UIButton) {
        stopButton.isHidden = false
        tapToRecord.text = "recording..."
        print("in recordAudio")
        
        let dirPath = NSSearchPathForDirectoriesInDomains(.documentDirectory, .userDomainMask, true)[0]
        
        
        let recordingName = "My_audio.wav"
        let pathArray = [dirPath, recordingName]
        let filePath = NSURL.fileURL(withPathComponents: pathArray)
        print(filePath)
        
        let session = AVAudioSession.sharedInstance()
        do {
            try session.setCategory(AVAudioSessionCategoryPlayAndRecord)
        } catch _ {
        }
        
        audioRecorder = try? AVAudioRecorder(url: filePath!, settings: [String: AnyObject]() )
        audioRecorder.delegate = self
        audioRecorder.isMeteringEnabled = true
        audioRecorder.prepareToRecord()
        audioRecorder.record()
        
    }
    
    // Identify if audio has finished recording before
    // performing any action in this audio
    
    func audioRecorderDidFinishRecording(recorder: AVAudioRecorder, successfully flag: Bool) {
        if(flag){
            let recordedAudio = RecordedAudio(filePathUrl: recorder.url as NSURL, title: recorder.url.lastPathComponent)
            performSegue(withIdentifier: "stopRecording", sender: recordedAudio)
        }else{
            print("Recording was not successful")
            recordButton.isEnabled = true
            stopButton.isHidden = true
        }
        
    }
    
    /* Perform a segue to the next view when the user
     presses on stopRecording */
    
    func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if(segue.identifier == "stopRecording"){
            let spRes:SpeechResultsVC = segue.destination as! SpeechResultsVC
            Alamofire.request("http://localhost:3333/api/", method: .post).responseJSON { response in
                
            }
        }
    }
    
    /* Stop recording when pressed the stop button */
    
    // TODO: keep pressed stop button to pause
    // implement audioRecord.pause() and labels for
    // user interface usability purposes.
    
    @IBAction func stopRecording(sender: UIButton) {
        audioRecorder.pause()
        let audioSession = AVAudioSession.sharedInstance()
        do {
            try audioSession.setActive(false)
        } catch _ {
        }
        audioRecorder.stop()
        
    }
    
    
    
}

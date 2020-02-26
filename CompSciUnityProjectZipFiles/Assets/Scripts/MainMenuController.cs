using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenuController : MonoBehaviour{
    // when called this method starts the game
    public void playGame(){
        SceneManager.LoadScene("GameScene");
        Time.timeScale = 1f;
        
    }

    // opens options menu when called
    public void options(){
        
    }
    // quits application when called
    public void exitGame(){
        Application.Quit();
    }

}

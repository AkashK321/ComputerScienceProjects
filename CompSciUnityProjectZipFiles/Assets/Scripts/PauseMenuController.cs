using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class PauseMenuController : MonoBehaviour{
    //declaring pause menu object
    public GameObject pauseMenuUI;

    // displays pause menu when called and unfreezes character's movement
    public void Resume(){
        Time.timeScale = 1f;
        pauseMenuUI.SetActive(false);
    }

    // opens menu scene when called
    public void Quit(){
        SceneManager.LoadScene("MenuScene");
    }
}

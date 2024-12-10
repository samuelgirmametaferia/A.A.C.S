using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public class MuseumTour : MonoBehaviour
{
    public GameObject[] artifacts;
    public ARSessionOrigin arOrigin;

    void Start()
    {
        arOrigin.session.trackingChanged += OnTrackingChanged;
    }

    void OnTrackingChanged(ARTrackingState trackingState)
    {
        if (trackingState == ARTrackingState.Tracking)
        {
            foreach (GameObject artifact in artifacts)
            {
                artifact.SetActive(true);
            }
        }
        else
        {
            foreach (GameObject artifact in artifacts)
            {
                artifact.SetActive(false);
            }
        }
    }
}
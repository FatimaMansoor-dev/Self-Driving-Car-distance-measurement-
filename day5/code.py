import torch 
import matplotlib.pyplot as plt
import cv2 


# download models
# model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
#model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

midas = torch.hub.load("intel-isl/MiDaS", model_type)
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
midas.to(device)
midas.eval()

## input transformation pipeline
tranforms = torch.hub.load('intel-isl/MiDas', 'transforms')
transform = tranforms.small_transform


## start webcam
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    ## transform input for midas
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgbatch = transform(img).to(device)

    # make prediction 
    with torch.no_grad():
        prediction = midas(imgbatch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img.shape[:2],
            mode="bicubic",
            align_corners=False
        ).squeeze()

        output = prediction.cpu().numpy()
        print(output)

    ## plot output
    plt.imshow(output)
    cv2.imshow('Frame', frame)

    plt.pause(0.00001)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.release()
        cv2.destroyAllWindows()

plt.show()

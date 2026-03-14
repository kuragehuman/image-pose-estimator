import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

with mp_pose.Pose(static_image_mode=False) as pose:

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = pose.process(image_rgb)

        if result.pose_landmarks:

            # 2D骨格をカメラ画像に描画
            mp_drawing.draw_landmarks(
                frame,
                result.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

        if result.pose_world_landmarks:

            landmarks = result.pose_world_landmarks.landmark

            xs = [-lm.x for lm in landmarks]
            ys = [lm.z for lm in landmarks]
            zs = [-lm.y for lm in landmarks]

            ax.cla()
            ax.view_init(elev=10, azim=90)

            ax.scatter(xs, ys, zs)

            # ボーンを描く
            for connection in mp_pose.POSE_CONNECTIONS:
                start = connection[0]
                end = connection[1]

                x = [xs[start], xs[end]]
                y = [ys[start], ys[end]]
                z = [zs[start], zs[end]]

                ax.plot(x, y, z)

            ax.set_xlim(-1, 1)
            ax.set_ylim(-1, 1)
            ax.set_zlim(-1, 1)

            plt.pause(0.001)

        cv2.imshow("camera", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
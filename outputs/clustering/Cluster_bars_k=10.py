import matplotlib.pyplot as plt
import numpy as np
import os

# --- ΡΥΘΜΙΣΕΙΣ ΦΑΚΕΛΟΥ ΑΠΟΘΗΚΕΥΣΗΣ ---
save_path = r'C:\Users\xrist\Desktop\Masters\Εξόρυξη και Προετοιμασία Δεδομένων\Εργασια\Φιλιππακης'

if not os.path.exists(save_path):
    os.makedirs(save_path)

# --- ΔΕΔΟΜΕΝΑ (k=10) ---
clusters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
legitimate = [164003 , 56484 , 35023 , 88427, 121685 ,117877  ,78796 , 39411 ,106027, 104864]
fraud = [   0  , 7760 ,34412   ,8861  ,  811 , 12738  , 1004   , 760  ,18940 ,  2117]

legit_arr = np.array(legitimate)
fraud_arr = np.array(fraud)

# --- ΔΗΜΙΟΥΡΓΙΑ ΓΡΑΦΗΜΑΤΟΣ ---
plt.figure(figsize=(12, 7))

# Μπάρες
plt.bar(clusters, legit_arr, label='Νόμιμες (0)', color='#3498db')
plt.bar(clusters, fraud_arr, bottom=legit_arr, label='Απάτες (1)', color='#e74c3c')

plt.title('Κατανομή Απάτης ανά Συστάδα (Clustering k=10)', fontsize=16)
plt.xlabel('Cluster ID', fontsize=14)
plt.ylabel('Πλήθος Συναλλαγών', fontsize=14)
plt.legend(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

# --- ΑΠΟΘΗΚΕΥΣΗ ΣΤΟΝ ΦΑΚΕΛΟ ΣΟΥ ---
full_filename = os.path.join(save_path, 'cluster_bars2.png')
plt.savefig(full_filename, dpi=300)
print(f"Η εικόνα αποθηκεύτηκε επιτυχώς στο: {full_filename}")

plt.show()
import matplotlib.pyplot as plt
import os

# --- ΡΥΘΜΙΣΕΙΣ ΦΑΚΕΛΟΥ ΑΠΟΘΗΚΕΥΣΗΣ ---
# Χρησιμοποιούμε r'' μπροστά για να διαβάσει σωστά τα backslashes των Windows
save_path = r'C:\Users\xrist\Desktop\Masters\Εξόρυξη και Προετοιμασία Δεδομένων\Εργασια\Φιλιπακης'

# Δημιουργία του φακέλου αν δεν υπάρχει
if not os.path.exists(save_path):
    os.makedirs(save_path)
    print(f"Δημιουργήθηκε ο φάκελος: {save_path}")

# --- ΔΕΔΟΜΕΝΑ ---
k_values = [6, 7, 8 ,9 ,10 ,11 ,12,13]
sse_values = [186805, 127963, 103333, 100312, 82166, 80325, 78695,77713,]

# --- ΔΗΜΙΟΥΡΓΙΑ ΓΡΑΦΗΜΑΤΟΣ ---
plt.figure(figsize=(10, 6))
plt.plot(k_values, sse_values, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)

plt.title('Μέθοδος Αγκώνα (Elbow Method)', fontsize=14)
plt.xlabel('Αριθμός Συστάδων (k)', fontsize=12)
plt.ylabel('Sum of Squared Errors (SSE)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(k_values)

plt.tight_layout()

# --- ΑΠΟΘΗΚΕΥΣΗ ΣΤΟΝ ΦΑΚΕΛΟ ΣΟΥ ---
full_filename = os.path.join(save_path, 'elbow_plot.png')
plt.savefig(full_filename, dpi=300)
print(f"Η εικόνα αποθηκεύτηκε επιτυχώς στο: {full_filename}")

plt.show()
const contractAddress = "0x8E6e34F439EedE36f4c8fB435511A6BD08E8a259";

const abi = [
  "function donate() payable",
  "function totalDonations() view returns (uint256)"
];

async function donate() {
  if (!window.ethereum) {
    alert("MetaMask tidak ditemukan");
    return;
  }

  const amount = document.getElementById("amount").value;
  if (!amount || amount <= 0) {
    alert("Masukkan jumlah ETH");
    return;
  }

  try {
    const provider = new ethers.BrowserProvider(window.ethereum);
    await provider.send("eth_requestAccounts", []);
    const signer = await provider.getSigner();

    const contract = new ethers.Contract(
      contractAddress,
      abi,
      signer
    );

    document.getElementById("status").innerText =
      "⏳ Menunggu konfirmasi MetaMask...";

    const tx = await contract.donate({
      value: ethers.parseEther(amount)
    });

    document.getElementById("status").innerText =
      "⛓️ Transaksi diproses di blockchain...";

    await tx.wait();

    document.getElementById("status").innerText =
      "✅ Donasi berhasil via Smart Contract! 🤍";

  } catch (err) {
    console.error(err);
    document.getElementById("status").innerText =
      "❌ Transaksi dibatalkan / gagal";
  }
}

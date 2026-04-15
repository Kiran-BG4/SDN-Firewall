from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.ipv4 import ipv4
from pox.lib.packet.tcp import tcp

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch connected!")

def _handle_PacketIn(event):
    packet = event.parsed

    # -------- PORT BASED FILTER --------
    tcp_packet = packet.find('tcp')
    if tcp_packet:
        dst_port = tcp_packet.dstport

        if dst_port == 80:
            log.info("Blocked HTTP (port 80)")

            with open("firewall_log.txt", "a") as f:
                f.write("BLOCKED PORT: HTTP (80)\n")

            return

    # -------- IP BASED FILTER --------
    ip_packet = packet.find('ipv4')
    if ip_packet:
        src = str(ip_packet.srcip)
        dst = str(ip_packet.dstip)

        if (src == "10.0.0.1" and dst == "10.0.0.2") or (src == "10.0.0.2" and dst == "10.0.0.1"):
            log.info(f"Blocked IP: {src} -> {dst}")

            with open("firewall_log.txt", "a") as f:
                f.write(f"BLOCKED IP: {src} -> {dst}\n")

            return

    # -------- ALLOW TRAFFIC --------
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

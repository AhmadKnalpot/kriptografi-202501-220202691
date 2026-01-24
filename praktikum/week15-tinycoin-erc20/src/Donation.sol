// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title Donation Smart Contract
/// @author Ramzi
/// @notice Contract untuk menerima donasi ETH
/// @custom:dev-run-script scripts/deploy.js
contract Donation {
    address public owner;
    uint256 public totalDonations;

    constructor() {
        owner = msg.sender;
    }

    function donate() external payable {
        require(msg.value > 0, "Donation must be greater than 0");
        totalDonations += msg.value;
    }

    function withdraw() external {
        require(msg.sender == owner, "Not owner");

        uint256 balance = address(this).balance;
        require(balance > 0, "No funds");

        (bool success, ) = payable(owner).call{value: balance}("");
        require(success, "ETH transfer failed");
    }
}

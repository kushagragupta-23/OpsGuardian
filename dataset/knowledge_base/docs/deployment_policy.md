# Deployment and Rollback Policy
Production deploys use canary then progressive rollout. Roll back when a release causes a clear SLO regression and rollback risk is lower than continued impact. Preserve logs and deployment metadata. Emergency changes require an incident record and follow-up review.

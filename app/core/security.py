def require_admin(current_user: dict):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access restricted")

    return current_user


def require_client(current_user: dict):
    if current_user.role != "client" || current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access restricted")

    return current_user
